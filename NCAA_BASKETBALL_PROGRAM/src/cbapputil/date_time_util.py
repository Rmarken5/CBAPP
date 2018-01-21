from datetime import datetime

def getTimeObjectFromString(input):

    if ':' in input:
        time_pieces = input.split(':')

        hour = time_pieces[0]
        second_half = time_pieces[1]

        second_half_peices = second_half.split(' ')
        if len(second_half_peices) > 1:
            if len(hour) == 1:
                hour = '0' + hour
            minutes = second_half_peices[0]
            indicator = second_half_peices[1].strip().upper()
            if hour == '12':
                hour = '00'
            if indicator == 'PM':
                hour = str((int(hour) + 12))
            	
            time_string = str(hour) + ':' +  minutes
            time_object = datetime.strptime(time_string, '%H:%M').time()
            
            return time_object
    return None

def getDateObjectFromString(input):

    if len(input.split('/')) == 3:
        date_object = datetime.strptime(input, '%Y/%m/%d')
        return date_object
	
if __name__ == '__main__':
    getTimeObjectFromString()
    getDateObjectFromString()	