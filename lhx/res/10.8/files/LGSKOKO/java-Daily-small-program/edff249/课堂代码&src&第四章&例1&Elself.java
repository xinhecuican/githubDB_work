package ������.��1; //�����·ݣ��ж������ڵļ���

public class Elself {

	private int month;      //������ǿɱ�ģ��ɱ������Ҫ��set/get�������Ա�����set��get
	private String season;  // season����Ҫ��õı������������û򴫲εı���������set/get����
                           //�������������set/get 
	
	public void setMonth(int month) { //ʲôʱ����set���ù��췽����������������
		this.month = month;           //set��ֻ��this.**=**; ��Ϊ�Զ�����
	}                                 //�������ж���������Ҫ�ж�ʱ����������������
                                      //һ��ͳ�ƶ��������static�������ڹ��췽���У�������΢���ӵ�����
	                                  //�����ڹ����У���Ϊ���췽���и�������㼶���������ã���ɰ�
	                                  //ֱ�Ӹ�ֵֻ�����ھֲ���������Ա��������ֱ�Ӹ�ֵ��
	                                  //�����Ա������ֱ�Ӹ�ֵ���������public�ġ��ڿ�Ҳ���Ա�һ����������
	                                  //����ֱ�Ӹ������public�ı����� 
	
	public int getMonth() {          
		return month;
	}

	public void judegeSeason(){                     //�ɲ����Դ�month�Ĳ���������ǣ��Ͳ���set
		if(month == 12 || month ==1 || month == 2)  //ע��==��=�������Լ�|��||������
			season = "Winter"; 
		else if (month == 3 || month ==4 || month == 5) //Ϊʲôelse�����һ��if��else�Ƿ�֮ǰ����
			season = "Spring";                          //if��else ��ʾ��������
		else if (month == 6 || month ==7 || month == 8) //if else if else �������Σ���ͨ������
			season = "Summer";                          //��Զ������һ��else��������һ���������
		                                                //if ֮��ֻ��һ����䣬���Բ���{}
		                                                //���е�if else if  else��һ�����壬
		                                                //��season = "Spring"֮��������������}
		                                                //���൱��֮ǰif else if���������ڣ�
		                                                //֮���else if �����
		else if (month == 9 || month ==10 || month == 11)
			season = "Autumn";
		else{
			season = "no season!";
		}
		System.out.println("month" + this.month + "belong to " + season);
		                             //this.month���Ը�Ϊthis.getMonth()
		                             //�������if�κΣ�������if��ǰ������if�ķ�

	}
}
