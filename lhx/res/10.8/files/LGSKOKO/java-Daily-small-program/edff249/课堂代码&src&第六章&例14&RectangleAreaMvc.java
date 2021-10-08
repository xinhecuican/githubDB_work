package 第六章.例14;

public class RectangleAreaMvc {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		WindowRectangle win = new WindowRectangle();
		win.setTitle("使用MVC计算矩形面积");			//不在构造方法中super（“”）,在这里用setTitle（"")
		win.setBounds(100, 100, 400, 200);
		

	}

}
