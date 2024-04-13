import gmailproject
import datefile
import addrfile
import mycal

mail = gmailproject.main()

s="' " + mail + " '"

##s='Your appointment for dental checkup is on March 16th,2020 at 5:00 pm. at Dr.Adsul ,Hospital, Gokhale road, Bandra .'


datefile.main(s)
##POS.main(s)
addrfile.main(s)
mycal.main()
