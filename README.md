# BenderModelToLaserCutSVG

Two simple scripts to turn a blender triangle model into an SVG laser cutter design for irl assembly. It's best used on low poly meshes without many tiny triangles, otherwise the assembly gets difficult. 

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
- The final SVG for laser cutting should be located in `/Blender_UVMap_VertexLabel_FromJSON/output.svg` that looks something like this:
  <img width="879" height="606" alt="image" src="https://github.com/user-attachments/assets/69a7f83a-8a0d-49c8-9b87-be8d4c899e74" />

  
(Note that for models with many small triangles, you will likely need to adjust the font size for the vertex labels.)

### Step 4, Laser-Cutting and Assembly
- Most laser cutters allow you to separate cutting and engraving paths by color. Engrave the red text and cut the black triangles.
- To assemble the model, arrange triangles around each vertex and glue or tape together triangles that share two vertex-numbers (an edge) in common.
- It works best if you bond them all lightly at first, then go over each joint with a stronger bond after the model is in the correct shape.
<img width="517" height="541" alt="image" src="https://github.com/user-attachments/assets/90cb6c22-0a85-4215-9742-8208b723b602" />


