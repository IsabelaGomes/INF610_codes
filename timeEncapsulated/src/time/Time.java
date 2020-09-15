package time;

/*
 * Representation of a time within a period of at most 24 hours.
 */
public interface Time {

	/**
	 * The number of hours is between 0 and 23.
	 * @return The number of hours.
	 */
	int getHour();

	/**
	 * The number of minutes is between 0 and 59.
	 * @return The number of minutes.
	 */
	int getMinute();
	
	/**
	 * The number of seconds is between 0 and 59.
	 * @return The number of seconds.
	 */
	int getSecond();
	
	/**
	 * Updates the number of hours.
	 * @param hour The new number of hours (0-23).
	 * @return true if the number was correctly updated.
	 */
	boolean setHour(int hour);

	/**
	 * Updates the number of minutes.
	 * @param minute The new number of minutes (0-59).
	 * @return true if the number was correctly updated.
	 */
	boolean setMinute(int minute);
	
	/**
	 * Updates the number of seconds.
	 * @param second The new number of seconds (0-59).
	 * @return true if the number was correctly updated.
	 */
	boolean setSecond(int second);
	
	/**
	 * Compares the current time with another time t.
	 * @param t The other time to compare with.
	 * @return -1, if the current time occurs before t;
	 * 1, if the current time occurs after t;
	 * 0, if the current time and t are equal.
	 */
	int compareTo(Time t);
	
	/**
	 * Returns the difference (in seconds) between the current time and t.
	 * If the current time occurs before t, the result will be negative.
	 * @param t The other time to calculate the difference.
	 * @return The difference (in seconds) between the current time and t.
	 */
	int difference(Time t);
	
	/**
	 * Builds a textual representation for the time.
	 * If the hour component is smaller than 12, the text must be ended with "AM".
	 * If the hour component is greater or equal 12, the text must be ended with "PM".
	 * If the hour component is greater than 12, the value shown must be (hour-12).
	 * @return The textual representation, using AM/PM.
	 */
	String toString();
	
}
