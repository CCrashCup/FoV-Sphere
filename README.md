# FoV-Sphere
A Blender add-on to be used for determining the correct Field of View (FoV) and Aspect Ratio (via the Width) when importing a scene that was ripped with Ninja Ripper 2.


To arrive at the correct import values, click on each numbered step in the panel, supplying the values where needed. There are a total of four (4) import steps, two (2) for each factor, FoV and Width. The same sphere mesh file will be used every time. Each import requires a different import value to be used. Make sure the imported mesh is the Active selected mesh. Before each subsequent import, delete the mesh, after all the steps before have been taken. To help keep track of where you are in the steps, each step is not active until the prior one has been done. The two (2) final values are flagged with red dots, which will turn green when each procedure successfully completes.

Note: Do NOT change the Height import value during this entire process, or the calculated final values will not be correct

Quick Use Chart.

1. 1st Import - Base (Reset)
   This clears all calculated and auto obtained values so you can start over. It retains user supplied values between runs.

2. Enter Base FoV_Y
   Enter the value from the first import.
