class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def print_interval(i):
    print("["+ str(i.start) + ", " + str(i.end) + "]", end='')


class Solution:
    def canAttendAllAppointments(self, appointments):
        can_attend_all_appointment = True

        if len(appointments) <= 1:
            return can_attend_all_appointment

        appointments.sort(key=lambda x: x.start)

        i, j = 0, 1
        while j < len(appointments):
            if appointments[i].end > appointments[j].start:
                can_attend_all_appointment = False
                break
            else:
                i = j
                j += 1

        return can_attend_all_appointment

def main():
    sol = Solution()
    print("Can attend all appointments: " +
          str(sol.canAttendAllAppointments([Interval(1, 4), Interval(2, 5), Interval(7, 9)])))
    print()

    print("Can attend all appointments: " +
          str(sol.canAttendAllAppointments([Interval(6, 7), Interval(2, 4),Interval(8, 12)])))
    print()

    print("Can attend all appointments: " +
          str(sol.canAttendAllAppointments([Interval(4, 5), Interval(2, 3), Interval(3, 6)])))
    print()

main()