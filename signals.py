from PyQt5.QtWidgets import QWidget,QLabel,QInputDialog,QFileDialog
from PyQt5.QtGui import QPixmap,QTransform
from PyQt5.QtCore import Qt,pyqtSignal
from functools import partial
import time
import os
from pynput.mouse import Listener
import pynput.mouse as pymouse
import pynput.keyboard as pykeyboard

class Signals:
	def sig_file_open(self):
		fname = QFileDialog.getOpenFileName(None,"Choisir un fichier", "","Données (*.csv *.txt)")
		if fname:
			if os.path.isfile(fname[0]): self.view_open_file(fname[0])

	def sig_process_data(self,data,grid):
		if self.error_manage(0X0002,self.x is None or self.y is None): return
		tel = self.tools_get_checked_widget(grid.get_widget_by_pos(2,0).layout())
		prenom = self.tools_get_checked_widget(grid.get_widget_by_pos(2,2).layout())
		welcome = grid.get_widget_by_pos(4,3).isChecked()
		d_from = grid.get_widget_by_pos(5,1).currentIndex()
		d_to = grid.get_widget_by_pos(5,3).currentIndex()
		message = grid.get_widget_by_pos(7,0).toPlainText()
		if welcome and self.error_manage(0x0001,self.check_is_empty(prenom),"prenom"): return
		prenom = prenom[0]
		if self.error_manage(0X0001,self.check_is_empty(message),"message"): return
		if self.error_manage(0X0001,self.check_is_empty(tel),"tel"): return
		self.subapp.showMinimized()
		mouse = pymouse.Controller()
		keyboard = pykeyboard.Controller()
		time.sleep(1)
		for index, row in data.iterrows():
			if index < d_from and index > d_to: continue
			for t in tel:
				time.sleep(1)
				mouse.position = (self.x,self.y)
				mouse.click(pymouse.Button.left,1)
				with keyboard.pressed(pykeyboard.Key.ctrl_l):
					keyboard.press('a')
					keyboard.release('a')
				keyboard.press(pykeyboard.Key.delete)
				time.sleep(0.5)
				self.tools_type_str(row[t.text()])
				time.sleep(1)
				keyboard.press(pykeyboard.Key.enter)
				keyboard.release(pykeyboard.Key.enter)
				time.sleep(0.5)
				if welcome:
					self.tools_type_str("Bonjour " + str(row[prenom.text()]).capitalize())
					keyboard.press(pykeyboard.Key.enter)
					keyboard.release(pykeyboard.Key.enter)
				self.tools_type_str(message)
				keyboard.press(pykeyboard.Key.enter)
				keyboard.release(pykeyboard.Key.enter)
		time.sleep(5)				
		self.subapp.showMaximized()
		self.u.txtBox("Messages Envoyés","Les messages ont été envoyés à toute votre liste de contact")

	def sig_pointer_on_click(self, x, y, button, pressed):
		if pressed:
			self.x = x
			self.y = y
			return False

	def sig_configure_pointer(self):
		self.u.txtBox("Configuration de la souris","Mettre le curseur sur la barre de recherche de whatsapp et cliquer gauche")
		self.subapp.showMinimized()
		with Listener(on_click=self.sig_pointer_on_click) as listener:
			listener.join()
		self.subapp.showMaximized()
		self.u.txtBox("Souris","La position de la souris a bien été enregistré")
