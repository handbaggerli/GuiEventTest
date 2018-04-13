/********************************************************************************
** Form generated from reading UI file 'dialogtext.ui'
**
** Created by: Qt User Interface Compiler version 5.6.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DIALOGTEXT_H
#define UI_DIALOGTEXT_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_DialogText
{
public:
    QVBoxLayout *verticalLayout;
    QTextEdit *textEdit;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *DialogText)
    {
        if (DialogText->objectName().isEmpty())
            DialogText->setObjectName(QStringLiteral("DialogText"));
        DialogText->resize(400, 300);
        verticalLayout = new QVBoxLayout(DialogText);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        textEdit = new QTextEdit(DialogText);
        textEdit->setObjectName(QStringLiteral("textEdit"));

        verticalLayout->addWidget(textEdit);

        buttonBox = new QDialogButtonBox(DialogText);
        buttonBox->setObjectName(QStringLiteral("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Close);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(DialogText);
        QObject::connect(buttonBox, SIGNAL(accepted()), DialogText, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), DialogText, SLOT(reject()));

        QMetaObject::connectSlotsByName(DialogText);
    } // setupUi

    void retranslateUi(QDialog *DialogText)
    {
        DialogText->setWindowTitle(QApplication::translate("DialogText", "Text Input", 0));
    } // retranslateUi

};

namespace Ui {
    class DialogText: public Ui_DialogText {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DIALOGTEXT_H
