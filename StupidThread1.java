
class StupidThread2 extends Thread {

	StupidThread1 t1;

	public StupidThread2(StupidThread1 stupidThread1) {
		t1 = stupidThread1;
	}

	public void run() {
		System.out.println("t2 is waiting...for t1 to finish");
		try {
			t1.join();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}

class StupidThread1 extends Thread {

	public void run() {

		StupidThread2 t2 = new StupidThread2(this);
		t2.start();

		System.out.println("t1 is waiting for t2 to finish...");
		try {
			t2.join();
			System.out.println("t2 finished...phew");
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	public static void main(String[] args) {

		StupidThread1 stupidThread1 = new StupidThread1();

		stupidThread1.start();

	}

}
