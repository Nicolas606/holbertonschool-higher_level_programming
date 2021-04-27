#include "lists.h"

/**
 * check_cycle -checks if a singly linked list has a cycle in it.
 *
 * @list: head of the sibgly linked list
 * Return: Always 0 (Success)
 */

int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *turtle = list;

	if (list == NULL)
		return (0);

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		turtle = turtle->next;

			if (turtle == hare)
				return (1);
	}
	return (0);

}
