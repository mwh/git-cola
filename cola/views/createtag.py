from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL

from cola import qt
from cola import qtutils
from cola.prefs import diff_font
from cola.views import standard


class CreateTag(standard.Dialog):
    def __init__(self, parent):
        standard.Dialog.__init__(self, parent=parent)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setWindowTitle(self.tr('Create Tag'))
        self.resize(506, 295)
        self._main_layt = QtGui.QVBoxLayout(self)
        self._main_layt.setContentsMargins(6, 12, 6, 6)

        # Form layout for inputs
        self._input_form_layt = QtGui.QFormLayout()
        self._input_form_layt.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)

        # Tag label
        self._tag_name_label = QtGui.QLabel(self)
        self._tag_name_label.setText(self.tr('Name'))
        self._input_form_layt.setWidget(0, QtGui.QFormLayout.LabelRole,
                                        self._tag_name_label)

        self.tag_name = QtGui.QLineEdit(self)
        self.tag_name.setToolTip(self.tr('Specifies the tag name'))
        self._input_form_layt.setWidget(0, QtGui.QFormLayout.FieldRole,
                                        self.tag_name)

        # Sign Tag
        self._sign_label = QtGui.QLabel(self)
        self._sign_label.setText(self.tr('Sign Tag'))
        self._input_form_layt.setWidget(1, QtGui.QFormLayout.LabelRole,
                                        self._sign_label)

        self.sign_tag = QtGui.QCheckBox(self)
        self.sign_tag.setToolTip(
                self.tr('Whether to sign the tag (git tag -s)'))
        self._input_form_layt.setWidget(1, QtGui.QFormLayout.FieldRole,
                                        self.sign_tag)
        self._main_layt.addLayout(self._input_form_layt)

        # Tag message
        self._tag_msg_label = QtGui.QLabel(self)
        self._tag_msg_label.setText(self.tr('Message'))
        self._input_form_layt.setWidget(2, QtGui.QFormLayout.LabelRole,
                                        self._tag_msg_label)
        # Exposed
        self.tag_msg = QtGui.QTextEdit(self)
        self.tag_msg.setAcceptRichText(False)
        self.tag_msg.setToolTip(self.tr('Specifies the tag message'))
        self.tag_msg.setFont(diff_font())
        self._input_form_layt.setWidget(2, QtGui.QFormLayout.FieldRole,
                                        self.tag_msg)
        # Revision
        self._rev_label = QtGui.QLabel(self)
        self._rev_label.setText(self.tr('Revision'))
        self._input_form_layt.setWidget(3, QtGui.QFormLayout.LabelRole,
                                        self._rev_label)
        # Exposed
        self.revision = QtGui.QComboBox(self)
        self.revision.setEditable(True)
        self.revision.setToolTip(self.tr('Specifies the SHA-1 to tag'))
        self._input_form_layt.setWidget(3, QtGui.QFormLayout.FieldRole,
                                        self.revision)

        # Buttons
        self._button_hbox_layt = QtGui.QHBoxLayout()
        self._button_spacer = QtGui.QSpacerItem(1, 1,
                                                QtGui.QSizePolicy.Expanding,
                                                QtGui.QSizePolicy.Minimum)
        self._button_hbox_layt.addItem(self._button_spacer)

        self.create_button = qt.create_button(text='Create Tag',
                                              icon=qtutils.git_icon())
        self._button_hbox_layt.addWidget(self.create_button)
        self._main_layt.addLayout(self._button_hbox_layt)

        self.close_button = qt.create_button(text='Close')
        self._button_hbox_layt.addWidget(self.close_button)

        self.connect(self.close_button, SIGNAL('clicked()'), self.accept)
