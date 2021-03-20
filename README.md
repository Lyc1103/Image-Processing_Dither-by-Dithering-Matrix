# Image-Processing_Dither-by-Dithering-Matrix
Step 1 :
  Use the dithering matrix D_2,
          D_2 = [   0 128  32 160 ]
                [ 192  64 224  96 ]
                [  48 176  16 144 ]
                [ 240 112 208  80 ]
  to generate an array D of image size by reprating D_2.
          D  =  [ D_2 D_2 D_2 ... D_2 ]
                [ D_2 D_2 D_2 ... D_2 ]
                [ D_2 D_2 D_2 ... D_2 ]
                ...
                [ D_2 D_2 D_2 ... D_2 ]
                
Step 2 :
  Threshold image I by
            I'(i, j) =  { 255    if I(i, j) >  D(i, j)
                        {  0     if I(i, j) <= D(i, j)
 
Step 3 :
  Show images I and I'
