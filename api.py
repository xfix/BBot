backend=getattr(__import__('backends.async'),'async')
class module():
    def __init__(self,address):
        self.__address__=address
    #Begin code from old api.py (requested by aj00200)
    def getConfigStr(cat,name):
    return config.c.get(cat,name)
def getConfigInt(cat,name):
    return config.c.getint(cat,name)
def getConfigFloat(cat,name):
    return config.c.getfloat(cat,name)
def getConfigBool(cat,name):
    return config.c.getboolean(cat,name)
def getHost(data):
    '''Returns the hostname (IP address) of the person who sent the message passed to the variable data'''
    return data[data.find('@')+1:data.find(' ')]
def getNick(data):
    '''Returns the nickname of the person who sent the message passed to this function'''
    return data[1:data.find('!')]
def getIdent(data):
    '''Returns the ident of the person who sent the message passed to this function'''
    return data[data.find('!')+1:data.find('@')]
def getMessage(data):
    '''Returns the actual message that was sent without the nickname, hostname, and so on'''
    return data[data.find(' :')+2:]
def hostInList(data,list):
    '''Tells you if the host of the person who sent the message that is pased as the first arg is in the list of hosts which is the second arg'''
    host=getHost(data)
    for su in list:
        if host.find(su)!=-1:
            return True
    else:
        return False
def checkIfSuperUser(data,superusers=config.superusers):
    return hostInList(data,superusers)
    #End code from old api.py
    def privmsg(self,nick,data,channel):
        '''Called every time a PRIVMSG is recieved'''
        print '* Go Message: (%s,%s,%s)'%(nick,data,channel)
    def append(self,channel,data=' '):
        print 'Use the NEW way to send things, msg(channel,data)'
    def msg(self,channel,data=' '):
        '''Send a message, data, to channel'''
        print 'PRIVMSG %s :%s'%(channel,data)
        backend.connections[self.__address__].push('PRIVMSG %s :%s\r\n'%(channel,data))
    def notice(self,channel,data):
        print ('NOTICE %s :%s'%(channel,data))
        backend.connections[self.__address__].push('NOTICE %s :%s'%(channel,data))
    def join(self,channel):
        backend.connections[self.__address__].push('JOIN %s'%channel)
    def part(self,channel):
        backend.connections[self.__address__].push('PART %s'%channel)
    def kick(self,channel,kickee,reason):
        backend.connections[self.__address__].push('KICK '+channel+' '+kickee+' :'+reason+'\r\n')
    def get_notice(self,nick,data,channel):
        '''Called every time a notice is recieved'''
        pass
    def get_join(self,nick,user,host,channel):
        pass
    def mode(channel,modes,nick=''):
        backend.connections[self.__address__].push('MODE '+channel+' '+modes+'\r\n')
    def raw(self,data):
        print '%s'%(data)
        backend.connections[self.__address__].push('%s\r\n'%(data))
