#include "lists.h"

/**
 * check_cycle - check if list has a cycle
 * @list: list
 *
 * Return: 0 if no, 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list, *temp;

	temp = head;
	while (temp->next != NULL)
	{
		temp = temp->next;
		if (temp->next == NULL)
			return (0);
		else if (temp->next == head)
			break;
	}
	return (1);
}
