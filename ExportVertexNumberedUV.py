import bpy
import os
import blf
import json

dat = bpy.context.active_object.data
uvMap = dat.uv_layers.active.data

blend_dir = os.path.dirname(bpy.data.filepath)
file_name = "UVMap.json"
file_path = os.path.join(blend_dir, file_name)

outputArray=[]
i=0
for loop in uvMap:
    outputArray.append([loop.uv[0],loop.uv[1],dat.loops[i].vertex_index])
    for poly in dat.polygons:
        if i>=poly.loop_start and i<(poly.loop_start+poly.loop_total):
            pIndex = poly.index
            xAvg = 0.0
            yAvg = 0.0
            
            for j in range(poly.loop_start, poly.loop_start + poly.loop_total):
                xAvg+=uvMap[j].uv[0]
                yAvg+=uvMap[j].uv[1]
                
            xAvg/=poly.loop_total
            yAvg/=poly.loop_total
            
            outputArray[i].append([xAvg,yAvg,pIndex])
            
            
        
    i=i+1 
    

json_data = json.dumps(outputArray)

 

# Write the JSON data to a file
with open(file_path, "w+") as f:
    f.write(json_data)
    



file_name = "UVMap.png"
file_path = os.path.join(blend_dir, file_name)

bpy.ops.uv.export_layout(filepath=file_path, size=(1024, 1024))

# Load the image back into Blender
img = bpy.data.images.load(filepath=file_path)

# Prompt the user with the "Save As" dialog
def save_image_as(img):
    original_area = bpy.context.area.type
    bpy.context.area.type = 'IMAGE_EDITOR'
    bpy.context.space_data.image = img
    bpy.ops.image.save_as('INVOKE_DEFAULT', copy=True)
    bpy.context.area.type = original_area


# Invoke the save as file dialog for the newly loaded image
save_image_as(img)

print("Export Completed!")

