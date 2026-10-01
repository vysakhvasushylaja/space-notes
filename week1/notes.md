# Week 1: Orbits

## What I learned
- A satellite is always falling, but it moves sideways so fast that it keeps missing the Earth.
- LEO is about 150-1000 km high. ISS is at about 400 km.
- Lower orbit = faster and shorter period. ISS: 7.67 km/s, 92.6 minutes per orbit.
- GEO is at 35,786 km. Its period is 24 hours, so it looks fixed in the sky.
- Period = distance of one orbit / speed.

## Labs
- `orbit.py`: calculates speed and period for any altitude, and the GEO altitude.
- `iss_pass.py`: predicts ISS passes over Guildford using a TLE from CelesTrak and Skyfield.
- `iss_passes.txt`: my results on 1 October 2026.

## What I found
- One ISS pass lasts only about 7 minutes.
- Passes come about every 97 minutes, a bit more than one orbit, because the Earth turns under the ISS.


## Security thought
TLEs are public, so an attacker can also know exactly when a satellite passes over them.
