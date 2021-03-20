# Image-Processing_Dither-by-Dithering-Matrix

***

## Step 1 : <br>
  Use the dithering matrix D_2, <br>
  D_2 = 
    <table border = '1'>
      <tr>
        <td>  0
        <td>128
        <td> 32
        <td>160
      <tr>
        <td>192
        <td> 64
        <td>224
        <td> 96
      <tr>
        <td> 48
        <td>176
        <td> 16
        <td>144
      <tr>
        <td>240
        <td>112
        <td> 208
        <td> 80
    </table>
  to generate an array D of image size by reprating D_2. <br>
  D  =  
    <table border = "1">
      <tr>
        <td>D_2
        <td>D_2
        <td>D_2
        <td>...
        <td>D_2
      <tr>
        <td>D_2
        <td>D_2
        <td>D_2
        <td>...
        <td>D_2
      <tr>
        <td>
        <td>...
        <td>
        <td>
        <td>...
      <tr>
        <td>D_2
        <td>D_2
        <td>D_2
        <td>...
        <td>D_2
   </table>
    
## Step 2 : <br>
  Threshold image I by <br>
  <table border = "0">
      <tr>
        <td>I'(i, j)
        <td>=
        <td>{
        <td>255
        <td>if I(i, j) >  D(i, j)
      <tr>
        <td>
        <td>
        <td>{
        <td>0
        <td>if I(i, j) <=  D(i, j)
   </table>
 
## Step 3 : <br>
  Show images I and I'
