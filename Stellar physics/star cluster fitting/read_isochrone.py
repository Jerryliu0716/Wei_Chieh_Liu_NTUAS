## Prepared for you below is a function that will
## read in the models from your uploaded isochrone file.
def read_isofile(filename, stellar_age = 11.0):

    # Every 0.5 Gyr from 5 Gyr to 15 Gyr
    # Every 0.25 Gyr from 1 Gyr to 5 Gyr
    # Set a minimum and maximum age range (in Gyrs) below:
    #minage = minage
    #maxage = maxage
    stellar_age = stellar_age
    sdss_u = []
    sdss_g = []
    sdss_r = []
    sdss_i = []
    sdss_z = []

    age = [] # in Gigayears
    mass = [] # ratio of stellar mass to M_sun
    logT = [] # log of the effective Temperature (K)
    logL = [] # log of the ratio of stellar luminosity to L_sun
    counter=0
    for line in open(filename).readlines():
        counter+=1
        cols = line.split()
        if (line.startswith('#')):
    #        print(counter, ': starts with hashtag: ',cols)
            if (counter >= 8):   # real data starts on line #8
                if ("AGE" in cols[0]):
                    block = (line[0:11])
                    thisage = float(block.split('=')[1])
    #                print("Reading stellar models with age: {0:.2f} Gyr".format(thisage))
        else:
            #if (thisage > minage) and (thisage < maxage):
            if thisage == stellar_age:
#                print(cols)
                if (len(cols) > 0):
                    age.append(thisage)
                    mass.append(float(cols[1]))
                    logT.append(float(cols[2]))
                    logL.append(float(cols[4]))
                    sdss_u.append(float(cols[5]))
                    sdss_g.append(float(cols[6]))
                    sdss_r.append(float(cols[7]))
                    sdss_i.append(float(cols[8]))
                    sdss_z.append(float(cols[9]))
    return (sdss_u, sdss_g, sdss_r, sdss_i, sdss_z, age, mass, logT, logL)

(sdss_u, sdss_g, sdss_r, sdss_i, sdss_z, age, mass, logT, logL) = read_isofile(isofile)
#(sdss_u2, sdss_g2, sdss_r2, sdss_i2, sdss_z2, age2, mass2, logT2, logL2) = read_isofile(isofile2)
#(sdss_u3, sdss_g3, sdss_r3, sdss_i3, sdss_z3, age3, mass3, logT3, logL3) = read_isofile(isofile3)
print("Read in {0:.0f} stellar models, age {1:.2f} Gyr.".format(len(sdss_u), age[0]))
