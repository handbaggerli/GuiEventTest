#ifndef DIALOGTEXT_H
#define DIALOGTEXT_H

#include <QDialog>

namespace Ui {
class DialogText;
}

class DialogText : public QDialog
{
    Q_OBJECT

public:
    explicit DialogText(QWidget *parent = 0);
    ~DialogText();

private:
    Ui::DialogText *ui;
};

#endif // DIALOGTEXT_H
