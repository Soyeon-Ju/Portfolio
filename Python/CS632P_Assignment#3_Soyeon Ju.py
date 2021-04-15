{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input numerator : 3\n",
      "Input denominator : 0\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "import logging\n",
    "\n",
    "logging.basicConfig(filename=\"Soyeon Ju_logfile.log\", level=logging.DEBUG,\n",
    "                        format='%(levelname)s: %(message)s')\n",
    "\n",
    "logging.basicConfig(\n",
    "format='%(levelname)s: %(message)s',\n",
    "level=logging.ERROR)\n",
    "\n",
    "logging.basicConfig(\n",
    "format='%(levelname)s: %(message)s',\n",
    "level=logging.INFO)\n",
    "\n",
    "logging.basicConfig(\n",
    "format='%(levelname)s: %(message)s',\n",
    "level=logging.CRITICAL)\n",
    "\n",
    "logging.basicConfig(\n",
    "format='%(levelname)s: %(message)s',\n",
    "level=logging.WARNING)\n",
    "\n",
    "def my_div(n, d):\n",
    "\n",
    "  try:\n",
    "\n",
    "    if (n % d == 0 and n!=0 and d!=0):   \n",
    "      logging.info('exact number')\n",
    "    elif (n % d != 0 and n!=0 and d!=0):  \n",
    "      logging.warning('rational or irrational number')\n",
    "    elif (n ==0 ):  \n",
    "      logging.error('')\n",
    "    else:\n",
    "      logging.debug('')\n",
    "  except ZeroDivisionError:\n",
    "    logging.critical('cannot divide by zero!')\n",
    "    return\n",
    "\n",
    "  return (n/d)\n",
    "\n",
    "n = int(input(\"Input numerator : \"))\n",
    "d = int(input(\"Input denominator : \"))\n",
    "\n",
    "print(my_div(n, d))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input numerator : 0\n",
      "Input denominator : 1\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "can only concatenate str (not \"int\") to str",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-26-b95527a71eb0>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     15\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0ma\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 17\u001b[0;31m     \u001b[0mlogging\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mERROR\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'ERROR '\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mmy_div\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mb\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     18\u001b[0m \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m     \u001b[0mlogging\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Warning'\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mmy_div\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mb\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
