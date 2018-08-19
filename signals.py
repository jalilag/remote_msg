from PyQt5.QtWidgets import QWidget,QLabel,QInputDialog,QFileDialog
from PyQt5.QtGui import QPixmap,QTransform
from PyQt5.QtCore import Qt,pyqtSignal
from functools import partial
import time
import os
import re
import shutil
from pynput.mouse import Listener
import pynput.mouse as pymouse
import pynput.keyboard as pykeyboard

class Signals:
	def sig_file_open(self):
		fname = QFileDialog.getOpenFileName(None,"Choisir un fichier", "","Données (*.csv *.txt)")
		if fname:
			if os.path.isfile(fname[0]): self.view_open_file(fname[0])

	def sig_process_data(self,data,grid):
		if self.x is None or self.y is None:
			self.u.txtBox("Erreur","Veuillez d'abord configurer la souris")
			return
		g_tel=grid.get_widget_by_pos(2,0).layout()
		g_prenom=grid.get_widget_by_pos(2,1).layout()
		tel = []
		prenom = None
		welcome = grid.get_widget_by_pos(4,1).isChecked()
		message = grid.get_widget_by_pos(6,0).toPlainText()
		for i in range(g_tel.count()):
			if g_tel.itemAt(i).widget().isChecked(): tel.append(g_tel.itemAt(i).widget().text())
		for i in range(g_prenom.count()):
			if g_prenom.itemAt(i).widget().isChecked(): prenom = g_prenom.itemAt(i).widget().text()
		if (welcome and prenom is None) or len(tel) == 0 or len(message) == 0:
			self.u.txtBox("Erreur","Un des champs tel, prenom, nom ou message est vide")
			return
		self.subapp.showMinimized()
		mouse = pymouse.Controller()
		keyboard = pykeyboard.Controller()
		time.sleep(1)
		for index, row in data.iterrows():
			for t in tel:
				time.sleep(1)
				mouse.position = (self.x,self.y)
				mouse.click(pymouse.Button.left,1)
				with keyboard.pressed(pykeyboard.Key.ctrl_l):
					keyboard.press('a')
					keyboard.release('a')
				keyboard.press(pykeyboard.Key.delete)
				time.sleep(0.5)
				self.tools_type_str(row[t])
				time.sleep(1)
				keyboard.press(pykeyboard.Key.enter)
				keyboard.release(pykeyboard.Key.enter)
				time.sleep(0.5)
				if welcome:
					self.tools_type_str("Bonjour " + str(row[prenom]).capitalize())
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
