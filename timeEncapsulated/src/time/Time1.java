package time;

/*
 * The time is represented by 3 integer values,
 * corresponding to the hour, minute and second components.
 */
public class Time1 extends AbstractTime implements Time {

	private int hour, minute, second;
	
	public Time1() {
		this.hour = this.minute = this.second = 0;
	}
	
	public Time1(int hour, int minute, int second) {
		setHour(hour);
		setMinute(minute);
		setSecond(second);
	}

	public int getHour() {
		return hour;
	}

	public int getMinute() {
		return minute;
	}

	public int getSecond() {
		return second;
	}

	public boolean setHour(int hour) {
		if (hour < 0 || hour > 23) {
			return false;
		}
		this.hour = hour;
		return true;
	}

	public boolean setMinute(int minute) {
		if (minute < 0 || minute > 59) {
			return false;
		}
		this.minute = minute;
		return true;
	}

	public boolean setSecond(int second) {
		if (second < 0 || second > 59) {
			return false;
		}
		this.second = second;
		return true;
	}
	
}
