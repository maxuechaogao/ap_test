# coding:utf-8
import types
from src.func.helper.log import log
__author__ = 'xcma'

log = log()
class ditchelper:

    path = []

    def replace_value(self,dict, objkey, value):
        self.path = []
        try:
            self.dict_get(dict, objkey)
            num = len(self.path)
            if num ==0:
                dict[objkey] = value
            elif num == 1:
                dict[self.path[0]][objkey] = value
            elif num == 2:
                dict[self.path[0]][self.path[1]][objkey] = value
            elif num == 3:
                dict[self.path[0]][self.path[1]][self.path[2]][objkey] = value
            elif num == 4:
                dict[self.path[0]][self.path[1]][self.path[2]][self.path[3]][objkey] = value
            else:
                msg ='{}>4'.format(num)
                log.error('{},{}'.format(msg,self.path))
                raise msg
            return dict
        except:
            log.error(msg)
            raise msg

    def dict_get(self, dict, objkey, default=False):
        """
        :param dict:
        :param objkey:
        :param default:
        :return:(True,0)
        """
        try:
            tmp = dict
            if tmp.has_key(objkey):
                default = True
                v = 1
                return default, v
            if tmp:
                for k, v in tmp.items():
                    if k == objkey:
                        default=True
                        return default,v
                    else:
                        if type(v) is types.DictType:
                            self.path.append(k)
                            ret = self.dict_get(v, objkey)
                            if ret is not default:
                                return ret

            try:
                return default,v
            except:
                return default, 0
        except BaseException as msg:
            raise msg

