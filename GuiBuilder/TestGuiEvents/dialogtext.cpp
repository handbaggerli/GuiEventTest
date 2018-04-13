#include "dialogtext.h"
#include "ui_dialogtext.h"

DialogText::DialogText(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogText)
{
    ui->setupUi(this);
}

DialogText::~DialogText()
{
    delete ui;
}
