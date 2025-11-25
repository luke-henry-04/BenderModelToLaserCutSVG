# BenderModelToLaserCutSVG

Two simple scripts to turn a blender triangle model into an SVG laser cutter design for irl assembly

# How to Use:
### Step 1, generating the undistorted, tightly packed UV map
- In Blender, select the model, go into Edit Mode, and select all faces.
- Run Triangulate Faces ( `CTRL + T` )
- Select all faces again and use Smart UV Project ( `U` ) with the following settings:
  
<img width="388" height="303" alt="image" src="https://github.com/user-attachments/assets/eb4467f7-c945-420e-a32b-414786670732" />
<br><br><br>


- In the UV editor, select all UV triangles and use Pack Islands with the following settings:
<img width="390" height="436" alt="image" src="https://github.com/user-attachments/assets/90524999-4b5f-4673-a81b-75393976c5cd" />

- Use the guides mednu in the UV editor to confirm that there is no distortion in angle or area.

### Step 2, exporting the UV data
- Select the scripting tab and open the file `ExportVertexNumberedUV.py`
- Click run while in edit mode with the whole model selected. 
- The script should have generated a file named `UVMap.json` in the directory with the current `.blend` file.

### Step 3, generating the final SVG
- The script `Blender_UVMap_VertexLabel_FromJSON.pde` is a Processing 4 sketch. You can download the IDE at Processing.org
- Place the generated `UVMap.json` file in the `/Blender_UVMap_VertexLabel_FromJSON/` directory with the script.
- Open `Blender_UVMap_VertexLabel_FromJSON.pde` in processing and run the sketch.
- The final SVG for laser cutting should be located in `/Blender_UVMap_VertexLabel_FromJSON/output.svg`
