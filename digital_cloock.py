class DigitalClock:
    def _init_(self, h: int = 0, m: int = 0, s: int = 0,) -> None:
        """ constucts a digital clock objet from three parameters (h,m,s)


        Args:
            h (int, optional): _description_. Defaults to 0.
            m (int, optional): _description_. Defaults to 0.
            s (int, optional): _description_. Defaults to 0.
        """
        assert h < 24 and h >= 0
        self.__h = h
        assert m < 60 and m >=0
        self.__m = m
        assert s < 60 and s >=0
        self.__s = s
    def get_time(self) -> tuple[int, int, int]: 
        """returns the current time the dijital clock holds
        returns:
        tuple[int, int, int]: return self.__h, self.__m   , self.__s"""

        return self.__h, self.__m   , self.__s   
    def clear_time(self) -> None: 
        """Clears the current time"""
        self.__h, self.__m   , self.__s = 0, 0, 0
    def increment(self) -> None:
        """sumary one second the current time
        """
        self.__h = self.__h + 1 if self.__m == 59 and self.__s == 59 else self.__h
        self.__h =0 if self.__h == 24 else self.__h
        self.__m = self.__m +1 if self.__s == 59 else self.__m
        self.__m = 0 if self.__m == 60 else self.__m
        self.__s = self.__s + 1 if self.__s < 59 else 0