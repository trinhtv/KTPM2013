public class test
{

	int giaipt (int a,int b){
		if(a ==0) return 0;
			int x = -b/a;
			//try{
				//return x;
				//
			//
		
	}

	static void test1(){

		int ketqua = giaipt(1,1);
		if(ketqua == -1 )
		{
			system.out.println("dung");

		}
		else{
			system.out.println("sai");

		}
	}
	static void test2(){

		int ketqua = giaipt(10,-90);
			
		if(ketqua == 9 )
		{
			system.out.println("dung");

		}
		else{
			system.out.println("sai");

		}
	}
	static void test3(){

		int ketqua = giaipt(0,1);
			
		if(ketqua == 9 )
		{
			system.out.println("dung");

		}
		else{
			system.out.println("sai");

		}
	}
	public static void main (String [] args){
			int x = giaipt(0,1);

		test1();
		test2();
		test3();
	}

}