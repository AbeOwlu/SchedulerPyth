Created a simple scheduler script using the json data files

Program is written for Python > 2.7. Preferrably > 3.0. 
Dependnecies list is in repo for libs in venv. 
No external libs were installed. Default python libs used

schedules each Teller to Customer with a few unoptimized assumption:
> the work day is a duration of 480 (min) for each Teller
> takes the total duration of Customer appointments for the work day 91715 (min)
> starts by matching specialty to service types, such that each Teller gets < 480 mins of total appointments
> then schedules whatever Customer is left to available Tellers without overscheduling one Teller over others.
> print out a work-day schedule for the tailers, with their assigned customer ids, total appointment duariont <480

Program was created with simplicity and speed in mind. Minimal attention wil be paid to modularity (re-usability using functions) and data veracity checks and security.
No external libraries were used to this effect. Allowing for implementing in any basic python environment

Features that are a must, but not implemented:
> Security implementation,
> Data deduping, veracity check, to ensure optimal scheduking.
