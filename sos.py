import npyscreen
import time

class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())
        self.registerForm("KOERS", BerekenKoers())
        self.registerForm("WATEROVERLAST", WaterOverlast())
        self.registerForm("PASSWORDGATE", PasswordGate())



class PasswordGate(npyscreen.Form):
    def create(self):
        self.add(npyscreen.FixedText, editable=False, value="Welkom, voor het wachtwoord in om toegang te krijgen tot het Ship Operating System!")
        self.password = self.add(npyscreen.TitlePassword, name="Wachtwoord:")
        #self.password.relx = 50
        #self.password.rely = 50
    
    def afterEditing(self):
        if self.password.get_value() == "COLOMBUS":
            self.parentApp.setNextForm("MAIN")
        else:
            npyscreen.notify_confirm(f"Fout wachtwoord!", title="Foutmelding")

class MainForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.FixedText, editable=False, value="SHIP OPERATING SYSTEM")
        #self.add(npyscreen.FixedText, rely=1, relx=-20, editable=False, value="version 3.14159265359")
        
        self.menu = self.add(npyscreen.TitleSelectOne, name="Selecteer je gewenste programma:", values=[
            "Bereken koers",
            "Instructies wateroverlast",
            "Detectiesysteem ijsbergen",
            "Torpedo lanceringsysteem",
            "Pong"
        ])

    # def afterEditing(self):
    #     self.parentApp.setNextForm(None)

    def afterEditing(self):
        if len(self.menu.get_value()) > 0:
            match self.menu.get_value()[0]:
                case 0:
                    self.parentApp.setNextForm("KOERS")
                case 1:
                    self.parentApp.setNextForm("WATEROVERLAST")
                case 2:
                    npyscreen.notify_confirm("Ijsbergdetectie module is niet geinstalleerd!", "Ongeldige keuze")
                    time.sleep(2)
                case 3:
                    npyscreen.notify_confirm("The program can’t start because TORPEDO.dll is missing from your computer.\nTry reinstalling Windows 95 to fix this problem.", "Ongeldige keuze")
                    time.sleep(2)
                case 4:
                    npyscreen.notify_confirm("Pong module is niet geinstalleerd!", "Ongeldige keuze")
                    time.sleep(2)    

class WaterOverlast(npyscreen.Form):
    def create(self):
        self.add(npyscreen.FixedText, editable=False, value="Instructies wateroverlast")
        self.add(
            npyscreen.TitlePager,
            editable=False,
            name="Instructies wateroverlast",
            values=["- Zet kraan V14 op 81%","- Zet kraan V27 op 72%","- Zet kraan V5 op  16% "]
        )
    
    def afterEditing(self):
        self.parentApp.switchFormPrevious()


#class CoordinaatEntry(npyscreen.TitleText):

class BerekenKoers(npyscreen.ActionFormV2):
    def create(self):
        self.add(npyscreen.FixedText, editable=False, value="KOERS BEREKENEN")
        self.locatie = self.add(npyscreen.TitleText, name="Coordinaat huidige locatie")
        self.bestemming = self.add(NumberInput, name="Coordinaat bestemming")
        self.add(
            npyscreen.TitlePager,
            name="Instructies koers instellen",
            editable=False,
            values=["Set autopilot uit", "Draai aan stuurwiel", "Stel gewesnte koers in", "Zet autopilot aan"]
        )
        #npyscreen.notify_confirm(f"Zet autopilot uit\nDraai aan stuurwiel\nStel gewenste koers in\nZet autopilot aan", title="Instructies koers instellen")
    
    def on_ok(self):
        try:
            locatie = int(self.locatie.get_value())
            bestemming = int(self.bestemming.get_value())
            koers = locatie * bestemming % 360
            npyscreen.notify_confirm(f"Koers: {koers}", title="Je berekende koers")
        except:
            npyscreen.notify_confirm(f"Niet alle waardes zijn ingevuld!", title="Foutmelding")

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

if __name__ == '__main__':
    TA = MyTestApp()
    TA.STARTING_FORM = TA.NEXT_ACTIVE_FORM = "PASSWORDGATE"
    TA.run()

