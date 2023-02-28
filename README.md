# FoV-Sphere
A Blender add-on to be used for determining the correct Field of View (FoV) and Aspect Ratio (via the Width) when importing a scene that was ripped with Ninja Ripper 2. Download here: https://github.com/CCrashCup/FoV-Sphere/releases


This is a two part process. The first part is for calculating the correct FoV_Y value to use when importing using World Space. The second part is for calculating the correct Width value to use when importing. Each part requires two (2) imports to be made with different test values. The resulting sphere mesh dimesions of these imports will be used in the calculations. To arrive at the correct import values, click on each numbered step in the panel, supplying the values used during the import where required. The same sphere mesh file will be used every time. Each import requires a different import value to be used. Make sure the imported mesh is the Active selected mesh. Before each subsequent import, delete the mesh, after all the steps before have been taken. To help keep track of where you are in the steps, each step is not active until the prior one has been done. The current step will be flagged with a yellow dot. The two (2) final values are flagged with red dots, which will turn green when each procedure successfully completes.

Note: Do NOT change the Height import value during this entire process, or the calculated final values will not be correct

Quick Use Chart (Normal Mode)

FoV_Y Calculator

1. 1st Import - Base (Reset)                                                  
   This clears all calculated and auto obtained values so you can start over. It retains user supplied values between runs. In the Importer settings, be sure to choose "Geometry Load:" [Reprojection (Full)]. Use the Width and Height values from the log file, or you can supply higher values for better precision.

2. Enter Base FoV_Y                                                   
   Enter the value from the first import.

3. 2nd Import - Test                                                        
   Ready to get another import with a different FoV_Y value.

4. Enter Test FoV_Y                                                            
   Enter the value from the second import.

5. Calculate FoV_Y                                                              
   Performs the calculation and puts the result in the next step.

6. Final FoV_Y                                                                   
   If it worked correctly, copy this value to use in the next import.

Width Calculator

7. 3rd Import - Base (Reset)                                                           
   This clears Width calculated and auto obtained values so you can redo. It retains user supplied values between runs. Be sure to use the FoV_Y value from step 8.

8. Enter Base Width                                                           
    Enter the value from the third import.

9. 4th Import - Test                                                                   
    Ready to get another import with a different Width value.

10. Enter Test Width                                                               
    Enter the value from the fourth import.

11. Calculate Width                                                            
    Performs the calculation and puts the result in the next step.

12. Final Width                                                            
    If it worked correctly, copy this value to use in the final import.

Now import one last time (hopefully) using the two calculated values. This time you will import all the meshes you need. To verify the results, select the original sphere object and check its dimensions.



Quick Use Chart (Expert Mode)

FoV_Y Calculator

1. 1st Import - Base (Reset)                                                  
   This clears all calculated and auto obtained values so you can start over. It retains user supplied values between runs. In the Importer settings, be sure to choose "Geometry Load:" [Reprojection (Full)]. Use the Width and Height values from the log file, or you can supply higher values for better precision.

2. Enter Base FoV_Y                                                   
   Enter the value from the first import.

3. Get Base YZ                                                               
   Make sure the mesh is selected. This obtains the needed values automatically.

4. 2nd Import - Test                                                        
   Ready to get another import with a different FoV_Y value.

5. Enter Test FoV_Y                                                            
   Enter the value from the second import.

6. Get Test Y                                                               
   Make sure the mesh is selected. This obtains the needed value automatically.

7. Calculate FoV_Y                                                              
   Performs the calculation and puts the result in the next step.

8. Final FoV_Y                                                                   
   If it worked correctly, copy this value to use in the next import.

Width Calculator

9. 3rd Import - Base (Reset)                                                           
   This clears Width calculated and auto obtained values so you can redo. It retains user supplied values between runs. Be sure to use the FoV_Y value from step 8.

10. Enter Base Width                                                           
    Enter the value from the third import.

11. Get Base X                                                                 
    Make sure the mesh is selected. This obtains the needed value automatically.

12. 4th Import - Test                                                                   
    Ready to get another import with a different Width value.

13. Enter Test Width                                                               
    Enter the value from the fourth import.

14. Get Test XZ                                                               
    Make sure the mesh is selected. This obtains the needed value automatically.

15. Calculate Width                                                            
    Performs the calculation and puts the result in the next step.

16. Final Width                                                            
    If it worked correctly, copy this value to use in the final import.

Now import one last time (hopefully) using the two calculated values. This time you will import all the meshes you need. To verify the results, select the original sphere object and check its dimensions.
