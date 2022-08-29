import torch
from PIL import Image
from torchvision import transforms

def predict(model, test_image_name):

    transform = image_transforms['test']

    test_image = Image.open(test_image_name)
    
    test_image_tensor = transform(test_image)
    if torch.cuda.is_available():
        test_image_tensor = test_image_tensor.view(1, 3, 224, 224).cuda()
    else:
        test_image_tensor = test_image_tensor.view(1, 3, 224, 224)
    
    with torch.no_grad():
        model.eval()
        # Model outputs log probabilities
        out = model(test_image_tensor)
        ps = torch.exp(out)

        topk, topclass = ps.topk(3, dim=1)
        
        mask = idx_to_class[topclass.cpu().numpy()[0][0]]
        unmask = idx_to_class[topclass.cpu().numpy()[0][0]]
        
        score_mask = topk.cpu().numpy()[0][0]
        score_unmask = topk.cpu().numpy()[0][0]
        
        if score_mask > score_unmask:
            result = mask
        else:
            result = unmask

        return [test_image, result]

        

image_transforms = { 
    'test': transforms.Compose([
        transforms.Resize(size=256),
        transforms.CenterCrop(size=224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ])
}

idx_to_class = {0: 'mask', 1: 'without_mask'}

