package time;

/*
 * The total time is represented by the number of seconds
 * starting at 0:00:00. For example, if "seconds" is 7265, then
 * the time represented is 2:01:05.
 */
public class Time2 extends AbstractTime implements Time {
	
	private int seconds;
	
	public Time2() {
		this.seconds = 0;
	}
	
	public Time2(int hour, int minute, int second) {
		seconds = hour*3600 + minute*60 + second;
	}

	public int getHour() {
		int hour = seconds/3600;
		return hour;
	}

	public int getMinute() {
		int minute = (seconds%3600)/60;
		return minute;
	}

	public int getSecond() {
		int second = seconds - getHour()*3600 - getMinute()*60;
		return second;
	}

	public boolean setHour(int hour) {
		if (hour < 0 || hour > 23) {
			return false;
		}
		int h = hour*3600;
		this.seconds = h + getMinute()*60 + getSecond();
		return true;
	}

	public boolean setMinute(int minute) {
		if (minute < 0 || minute > 59) {
			return false;
		}
		int m = minute*60;
		this.seconds = getHour()*3600 + m + getSecond();
		return true;
	}

	public boolean setSecond(int second) {
		if (second < 0 || second > 59) {
			return false;
		}
		this.seconds = getHour()*3600 + getMinute()*60 + second;
		return true;
	}
	
}
