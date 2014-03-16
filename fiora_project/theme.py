from random import randint
class Theme(object):
    
    def __init__(self, css_class, weapon, gender, quote):
        self.css_class = css_class
        self.weapon = weapon
        self.gender = gender
        self.quote = quote
        
    @staticmethod
    def get_by_css_class(css_class):
        for theme in Theme.THEMES:
            if theme.css_class == css_class:
                return theme
            
    @staticmethod
    def get_by_values(gender, weapon):
        for theme in Theme.THEMES:
            if theme.gender == gender and theme.weapon == weapon:
                return theme
            
    @staticmethod
    def get_random_theme():
        return Theme.THEMES[randint(0, len(Theme.THEMES)-1)]
   
Theme.THEMES = (
    Theme('blitz', 'F', 'R', "Metal is harder than flesh."),
    Theme('cait', 'G', 'F', "Who doesn't like to be under the gun?"),
    Theme('fiora', 'B', 'F', "They dare not strike back."),
    Theme('garen', 'B', 'M', "Victory awaits."),
    Theme('karthus', 'R', 'M', "My song is death."),
    Theme('lee', 'F', 'M', "Act free of doubt."),
    Theme('lucian', 'G', 'M', "We're gonna need more coffins."),
    Theme('oriana', 'R', 'R', "I know what makes them tick. I know how to make the ticking stop."),
    Theme('rammus', 'B', 'R', "OK."),
    Theme('sona', 'R', 'F', "Shall we resolve this dissonance?"),
    Theme('urgot', 'G', 'R', "They will know fear."),
    Theme('vi', 'F', 'F', "One girl wrecking crew."),
)