import sys
from route_class import NextBus


def main():
    next_bus = NextBus()
    bus_route = next_bus.get_route(sys.argv[1])
    if not bus_route:
        print('{} route was not found'.format(sys.argv[1]))
        exit()
    direction = next_bus.get_direction(sys.argv[3])
    if not direction:
        print('{} is incorrect for this route.'.format(sys.argv[3]))
        exit()
    bus_stop = next_bus.get_bus_stop(bus_route,direction,sys.argv[2])
    if not bus_stop:
        print('{} bustop was not found'.format(sys.argv[2]))
        exit()
    get_next_trip_timestamp = next_bus.get_next_trip_timestamp(bus_route,direction,bus_stop)
    if not get_next_trip_timestamp:
        exit()
    mins = next_bus.calculate_time(get_next_trip_timestamp)
    if int(mins) > 1:
        print('{} Minutes'.format(mins))
    elif int(mins) == 1:
        print('{} Minute'.format(mins))
    else:
        exit()


if __name__ == '__main__':
    main()
