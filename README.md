# FoV-Sphere
A Blender add-on to be used for determining the correct Field of View (FoV) and Aspect Ratio (via the Width) when importing a scene that was ripped with Ninja Ripper 2. Download here: https://github.com/CCrashCup/FoV-Sphere/releases


This is a two part process. The first part is for calculating the correct FoV_Y value to use when importing using World Space. The second part is for calculating the correct Width value to use when importing. Each part requires two (2) imports to be made with different test values. The resulting sphere mesh dimesions of these imports will be used in the calculations. To arrive at the correct import values, click on each numbered step in the panel, supplying the values used during the import where required. The same sphere mesh file will be used every time. Each import requires a different import value to be used. Make sure the imported mesh is the Active selected mesh. Before each subsequent import, delete the mesh, after all the steps before have been taken. To help keep track of where you are in the steps, each step is not active until the prior one has been done. The current step will be flagged with a yellow dot. The two (2) final correct values are flagged with red dots, which will turn green when each procedure successfully completes.

Note: Do NOT change the Height import value during this entire process, or the calculated final values will not be correct

Quick Use Chart (Normal Mode)

FoV_Y Calculator

1.  Do 1st FoV_Y Import (Reset)                                                                            
   In the Importer settings, be sure to choose "Geometry Load:" [Reprojection (Full)]. Use the Width and Height values from the log file, or you can supply higher values for better precision.

2. Enter FoV_Y used                                                                            
   Enter the value from the first FoV_Y import.

3. Do 2nd FoV_Y Import                                                                            
   Ready to get another import with a different FoV_Y value.

4. Enter FoV_Y used                                                                            
   Enter the value from the second FoV_Y import.

5. Do FoV_Y Calculation                                                                            
   Performs the calculation and puts the result in the next step.

6. Correct FoV_Y                                                                            
   If it worked correctly, copy this value to use for all imports of this scene.
   

Width Calculator

7. Do 1st Width Import (Reset)                                                                            
   Be sure to use the Correct FoV_Y value from the previous calculation.

8. Enter Width used                                                                            
    Enter the value from the first Width import.

9. Do 2nd Width Import                                                                            
    Get another import using a different Width value.

10. Enter Width used                                                                            
    Enter the value from the second Width import.

11. Do Width Calculation                                                                            
    Performs the calculation and puts the result in the next step.

12. Correct Width                                                                            
    If it worked correctly, copy this value to use for all imports of this scene.

Now import one last time (hopefully) using the two calculated values. This time you will import all the meshes you need. To verify the results, select the original sphere object and check its dimensions.


# Step by step instructions without explanation.

Import the sphere mesh file with the first FoV value and the first Width and Height. Never change the Height value once you start.

Click Step 1.

Enter the first FoV value from the first import into Step 2. Press ENTER.

Delete the mesh.

Import the sphere mesh file with the second FoV value and the same Width and Height.

Click step 3.

Enter the second FoV value from the second import into Step 4. Press ENTER.

Click Step 5.

Copy the calculated FoV Value from Step 6. Press ENTER.

Delete the mesh.

Import the sphere mesh file with the copied calculated FoV value and the same Width and Height.

Click Step 7.

Enter the first Width value from the third import into Step 8. Press ENTER.

Delete the mesh.

Import the sphere mesh file with the copied calculated FoV value and the second Width, but with the same Height.

Click step 9.

Enter the second Width value from the fourth import into Step 10. Press ENTER.

Click Step 11.

Copy the calculated Width Value from Step 12.

Delete mesh.

Import all the mesh files with the copied calculated FoV value and the copied calculated Width value with the same Height.

Done. 

