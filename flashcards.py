#!/usr/bin/env python

import click


@click.group()
def flashcards():
    pass


@click.command()
@click.argument("front")
@click.argument("back")
def new_flashcard(front, back):
    """Create a new flashcard

    FRONT is the question on the card.
    BACK is the information on the back of the card.
    """
    pass


@click.command()
def list_flashcards():
    """List flashcards by card number and card fronts.
    """
    pass


@click.command()
@click.argument("card_number", type=int)
def delete_flashcard(card_number):
    """Delete a flashcard

    CARD_NUMBER is the number displayed before the question when running the `list` command.
    """
    pass


@click.command()
@click.argument("number_of_cards", default=10, type=int)
def practice(number_of_cards):
    """Present flashcards to study.

    NUMBER_OF_CARDS is the number of questions to ask. Defaults to 10.
    """
    pass


flashcards.add_command(new_flashcard, "new")
flashcards.add_command(list_flashcards, "list")
flashcards.add_command(delete_flashcard, "delete")
flashcards.add_command(practice, "practice")

if __name__ == "__main__":
    flashcards()
