# video2frame_tool
This program is used to extract frames from the video.


The input files：

input_dir/

         video_files/
         
                    vidoe_name
                    
         .../
         
            ...
            
            
For example,

UCF_101/

       ApplyEyeMakeup/
       
                      v_ApplyEyeMakeup_g01_c01.avi
                      
                      
The output files：

output_dir/

         video_files/
         
                    vidoe_name/
                    
                              frame_name
                              
         .../
         
            ...
            
            
For example,

UCF_101/

       ApplyEyeMakeup/
       
                      v_ApplyEyeMakeup_g01_c01/
                      
                                              00001.jpg
                                              
 
You can also change interval to extract frames by setting different values of extraction_interval, and we also set the minmum of the total frames, change this to any value you need.
