import os
from ij import IJ, Prefs
from ij.plugin import ChannelSplitter
from ij.io import FileSaver
 
# open folder
folder_path = "Stained images cells"
output_path = "new"
# Loop through files in folder
for filename in os.listdir(folder_path):
    if filename.endswith(".tif"):
        # Open the image
        imp = IJ.openImage(os.path.join(folder_path, filename))
        # Split channels
        channels = ChannelSplitter.split(imp)
        # Save red channel as new image
        red_channel = channels[0]  # Select the red channel
        output_filename = os.path.splitext(filename)[0] + "_red.tif"
        output_file_path = os.path.join(output_path, output_filename)
        imp.close()
        # Apply operations to the red channel
        IJ.run(red_channel, "Enhance Contrast...", "saturated=0.35 normalize")
        IJ.run(red_channel, "Subtract Background...", "rolling=100 light")
        IJ.run(imp, "Enhance Contrast...", "saturated=0.35 normalize")
        IJ.run(imp, "Gaussian Blur...", "sigma=3")
        IJ.setAutoThreshold(imp, "Default dark no-reset")
        IJ.setAutoThreshold(imp, "Otsu dark no-reset")
        Prefs.blackBackground = True;
        IJ.setRawThreshold(imp, 130, 255)
        IJ.run(red_channel, "Convert to Mask", "")
        image2 = IJ.run(red_channel, "Analyze Particles...", "size=4000-20000 circularity=0.50-1.00 show=Masks exclude clear")
        Prefs.blackBackground = True
        image2 = IJ.run("Invert")
        binaryMask = IJ.getImage(image2)
        fs = FileSaver(binaryMask)
        fs.saveAsTiff(output_file_path)
        IJ.run("Close")