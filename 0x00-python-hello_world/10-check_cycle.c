#include "lists.h"

/**
 * check_cycle - floyd cycle detection algorithm
 * @list: singly linked list to be checked
 * Return: 0 if no cycle found, 1 if cycle found
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	if (list == NULL || list->next == NULL)
		return (0);  /*No cycle if list is empty or has only one node*/

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;  /* Move hare two steps ahead */
		tortoise = tortoise->next;  /* Move tortoise one step ahead */

		if (tortoise == hare)
			return (1);  /* Cycle detected */
	}

	return (0);  /* No cycle found */
}
