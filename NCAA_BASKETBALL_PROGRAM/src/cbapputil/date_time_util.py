from datetime import datetime

def getTimeObjFromDTString(input):

    if input is not None and ':' in input and ' ' in input:
        date_time_parts = input.split(' ')
        if len(date_time_parts) > 1:
            time_string = date_time_parts[1]
            timeObject = datetime.strptime(time_string, '%H:%M').time()
            return timeObject
    return None        

def getTimeObjectFromString(input):
    print ('getTimeObjectFromString: ' +  input)
    #2018-02-08 19:20
    if ':' in input:
        time_pieces = input.split(':')
        # time_string = time_pieces[1]

        hour = time_pieces[0]
        minutes = time_pieces[1]
        print(hour)
        print (minutes)
        
        second_half_peices = minutes.split(' ')
        minutes = second_half_peices[0]
        if len(hour) == 1:
            hour = '0' + hour
        
        indicator = second_half_peices[1].strip().upper()
        if hour == '12':
            hour = '00'
        if indicator == 'PM':
            hour = str((int(hour) + 12))
        	
        #print(time_string)    
        time_string = hour + ':' + minutes
        time_object = datetime.strptime(time_string, '%H:%M').time()
        # print(time_object)    
        return time_object
    return None

def getDateObjectFromString(input):
    
    if len(input.split('-')) == 3:
        date_parts = input.split(' ')
        date = date_parts[0]
        date_object = datetime.strptime(date, '%Y-%m-%d').date()
        return date_object
	
if __name__ == '__main__':
    getTimeObjectFromString()
    getDateObjectFromString()	