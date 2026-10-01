from skyfield.api import load, wgs84

ts = load.timescale()
url = 'https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=TLE'
iss = load.tle_file(url, filename='iss.tle', reload=True)[0]
print(iss)

guildford = wgs84.latlon(51.236, -0.570)
t0 = ts.now()
t1 = t0 + 1  # next 24 hours

times, events = iss.find_events(guildford, t0, t1, altitude_degrees=10.0)
names = ['rises (AOS)', 'highest point', 'sets (LOS)']
for t, e in zip(times, events):
    alt, az, dist = (iss - guildford).at(t).altaz()
    print(t.utc_strftime('%Y-%m-%d %H:%M:%S UTC'), names[e],
          f'elevation {alt.degrees:.0f} deg, distance {dist.km:.0f} km')
