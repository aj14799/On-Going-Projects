import PIL
from PIL import Image

def convert_pdf_2_image(uploaded_image_path, uploaded_image,img_size):
    project_dir = os.getcwd()
    os.chdir(uploaded_image_path)
    file_name = str(uploaded_image).replace('.pdf','')
    output_file = file_name+'.jpg'
    pages = convert_from_path(uploaded_image, 200)
    for page in pages:
        page.save(output_file, 'JPEG')
        break
    os.chdir(project_dir)
    img = Image.open(output_file)
    img = img.resize(img_size, PIL.Image.ANTIALIAS)
    img.save(output_file)
    return output_file