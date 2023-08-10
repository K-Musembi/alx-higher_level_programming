#include "lists.h"

/**
 * insert_node - insert number into sorted list
 * @head: list head pointer
 * @number: number to insert
 *
 * Return: address of node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(int) * number);
	listint_t *temp = *head, *nxt;

	if (node == NULL)
		return (NULL);

	node->n = number;
	while (temp->next != NULL)
	{
		if (temp->n < node->n)
			nxt = temp;
		temp = temp->next;
		if (temp->n > node->n)
		{
			nxt->next = node;
			node->next = temp;
			break;
		}
	}
	return (node);
}
