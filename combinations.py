
from itertools import product

image = gimp.image_list()[0]
out_path = '/Users/antonkrutikov/Downloads/out'
file_base_name = 'temp'

def make_variants(image):
    groups = []
    for layer in image.layers:
        if isinstance(layer, gimp.GroupLayer):
            groups.append(layer.layers)
    return list(product(*groups))

def hide_all(image):
    for layer in image.layers:
        if isinstance(layer, gimp.GroupLayer):
            for inner_layer in layer.layers:
                inner_layer.visible = False

def save(image, out_path):
    variants = make_variants(image)
    for i,v in enumerate(variants):
        hide_all(image)
        for l in v:
            l.visible = True
        new_image = pdb.gimp_image_duplicate(image)
        new_layer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
        pdb.gimp_file_save(new_image, new_layer, '%s/%s_%s.png' % (out_path,file_base_name,i), '?')
        pdb.gimp_image_delete(new_image)

save(image, out_path)