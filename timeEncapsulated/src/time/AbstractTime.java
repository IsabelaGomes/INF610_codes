package time;

public abstract class AbstractTime implements Time {

	public int compareTo(Time t) {
		if (getHour() > t.getHour()) {
			return 1;
		} else if (getHour() < t.getHour()) {
			return -1;
		} else if (getMinute() > t.getMinute()) {
			return 1;
		} else if (getMinute() < t.getMinute()) {
			return -1;
		} else if (getSecond() > t.getSecond()) {
			return 1;
		} else if (getSecond() < t.getSecond()) {
			return -1;
		} else {
			return 0;
		}
	}

	public int difference(Time t) {
		int s1 = 3600*getHour() + 60*getMinute() + getSecond();
		int s2 = 3600*t.getHour() + 60*t.getMinute() + t.getSecond();
		return s1 - s2;
	}

	public String toString() {
		return (getHour() <= 12 ? getHour() : getHour()-12)
				+ ":"
				+ (getMinute() < 10 ? "0" : "") + getMinute()
				+ ":"
				+ (getSecond() < 10 ? "0" : "") + getSecond()
				+ (getHour() < 12 ? " AM" : " PM")
				;
	}
	
}
