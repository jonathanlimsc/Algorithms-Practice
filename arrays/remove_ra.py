def process_ra():
    '''
    Removes all instances of 'ra' in input_str
    '''
    input_str = raw_input()
    if input_str == None or len(input_str) == 0:
        print "\n"
        return
    print ''.join(input_str.split('ra')) + "\n"


# print process_ra('taberareruderarerumirareru') == 'tabererudererumireru'
# print "Should be tabererudererumireru"
#
# print process_ra('rraarraarraa') == 'rarara'
# print "Should be rarara"
#
# print process_ra('recruitsummerintern') == 'recruitsummerintern'
# print "should be recruitsummerintern"

# print process_ra(None)
# print process_ra("")
