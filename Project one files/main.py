{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'AnimalShelter'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-326e98a45174>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mAnimalShelter\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mAnimalShelter\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0ma\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mAnimalShelter\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m animal_data = [\n\u001b[1;32m      5\u001b[0m     {\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'AnimalShelter'"
     ]
    }
   ],
   "source": [
    "from AnimalShelter import AnimalShelter\n",
    "\n",
    "a = AnimalShelter()\n",
    "animal_data = [\n",
    "    {\n",
    "        \"name\":\"bruno\",\n",
    "        \"type\":\"dog\"\n",
    "    },\n",
    "    {\n",
    "        \"name\":\"missy\",\n",
    "        \"type\":\"cat\"\n",
    "    },\n",
    "    {\n",
    "        \"name\":\"sticky\",\n",
    "        \"type\":\"dog\"\n",
    "    }\n",
    "]\n",
    "\n",
    "for i in animal_data:\n",
    "    a.create(i)\n",
    "\n",
    "dogs = a.read( {\"type\":\"dog\"}  )\n",
    "for dog in dogs:\n",
    "    print(dog)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
