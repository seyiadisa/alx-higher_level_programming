#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle
 * @list: pointer to beginning of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *turtle = list;

	while (hare->next != NULL)
	{
		turtle = turtle->next;
		hare = hare->next->next;

		if (hare == NULL)
			return (0);

		if (turtle == hare)
			return (1);
	}

	return (0);
}
