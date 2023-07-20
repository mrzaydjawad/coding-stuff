#include <SFML/Graphics.hpp>
#include <iostream>
#include <iomanip>
#include <ctime> // for time functions

using namespace std;

// Function to check if a given year is a leap year
bool isLeapYear(int year) {
    return ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0);
}

// Function to get the number of days in a given month and year
int getDaysInMonth(int month, int year) {
    static const int daysInMonth[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    return (month == 2 && isLeapYear(year)) ? 29 : daysInMonth[month];
}

// Function to display the calendar for a specific month and year
void displayCalendar(sf::RenderWindow& window, int month, int year) {
    // SFML Text for the month and year header
    sf::Font font;
    font.loadFromFile("E:/coding and wor/coding/cpp/cpp code/fonts/arial.ttf"); // Replace with the path to your font file
    sf::Text header;
    header.setFont(font);
    header.setCharacterSize(24);
    header.setString(to_string(year) + " - " + to_string(month));
    header.setPosition(20.f, 20.f);

    // SFML Text for the days of the week
    sf::Text daysOfWeek;
    daysOfWeek.setFont(font);
    daysOfWeek.setCharacterSize(18);
    daysOfWeek.setString("SUN  MON  TUE  WED  THU  FRI  SAT");
    daysOfWeek.setPosition(20.f, 60.f);

    // Calculate the day of the week for the 1st day of the month
    tm timeIn = {0, 0, 0, 1, month - 1, year - 1900};
    mktime(&timeIn);
    int dayOfWeek = timeIn.tm_wday;

    // SFML Text for the days of the month
    sf::Text days;
    days.setFont(font);
    days.setCharacterSize(18);
    days.setPosition(20.f, 100.f);

    // Build the string for the days of the month
    string daysString;
    int daysInMonth = getDaysInMonth(month, year);
    for (int day = 1; day <= daysInMonth; day++) {
        daysString += to_string(day) + " ";

        // Move to the next line after Saturday
        if ((day + dayOfWeek) % 7 == 0)
            daysString += "\n";
    }
    days.setString(daysString);

    // SFML Text for current time and date
    sf::Text currentTime;
    currentTime.setFont(font);
    currentTime.setCharacterSize(16);
    currentTime.setPosition(20.f, window.getSize().y - 50.f);

    // Clear the window and draw the calendar elements
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // Update current time and date every second
        time_t now = time(0);
        tm* currentTimeInfo = localtime(&now);
        stringstream timeStr;
        timeStr << put_time(currentTimeInfo, "%F %T"); // Format: yyyy-mm-dd HH:MM:SS
        currentTime.setString("Current Time: " + timeStr.str());

        window.clear(sf::Color::White);
        window.draw(header);
        window.draw(daysOfWeek);
        window.draw(days);
        window.draw(currentTime);
        window.display();

        sf::sleep(sf::seconds(1)); // Wait for 1 second before updating the time
    }
}

int main() {
    int month, year;

    // Get the month and year from the user
    cout << "Enter month (1-12): ";
    cin >> month;
    cout << "Enter year: ";
    cin >> year;

    // Create an SFML window
    sf::RenderWindow window(sf::VideoMode(500, 400), "Calendar");

    // Display the calendar for the specified month and year
    displayCalendar(window, month, year);

    return 0;
}

