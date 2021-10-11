package br.com.ibta.tcc.main;

import ij.ImagePlus;
import ij.io.Opener;

import java.io.File;

import net.imglib2.img.Img;
import net.imglib2.type.NativeType;
import net.imglib2.type.numeric.NumericType;

public class Image {

	private String path_image;
	private Image image;
	
	public Image(String path){
		
		this.path_image = path;
		
	}
	
	public String getPath_image() {
		return path_image;
	}

	public void setPath_image(String path_image) {
		this.path_image = path_image;
	}

	public < T extends NumericType< T > & NativeType< T > > Image(){
		File file = new File( "DrosophilaWing.tif" );
		 
        // open a file with ImageJ
        //final ImagePlus imp = new Opener().openImage( file.getAbsolutePath() );
 
        // display it via ImageJ
        //imp.show();
 
     // 
	}
	
}
