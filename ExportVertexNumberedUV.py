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
    
print("Export Completed!")


